from kafka import KafkaConsumer
from conf.access_config import property

class OffsetChoice:
    def __init__(self):
        self.c = KafkaConsumer(
            property.access_config('topic_name'),
            bootstrap_servers = property.access_config('server'), 
            group_id = property.access_config('consumer_group')
        )
        
    
    ### FOR DISPLAY ------------------------------------------------
    def get_total_offset(self, partitions_set):
        # offsets_dict = self.c.beginning_offsets(partitions_set) 
        offsets_dict = self.c.end_offsets(partitions_set) # A set of partitions 
                                       # assigned to the consumer.
                                       # use self.c.assignment()

        for partition, total_offset in offsets_dict.items():
            print(f'Partition {partition}: {total_offset} Offsets')
    
    
    
    ### O_N will be [i] in a for loop ---------------------------------
    def get_specified_offset(self, partition_number, offset_number): 
        offset_value = self.c.seek(partition_number, offset_number)
        
        print(offset_value)
        return offset_value
        
        """Manually specify the fetch offset for a TopicPartition.

        Overrides the fetch offsets that the consumer will use on the next
        :meth:`~kafka.KafkaConsumer.poll`. If this API is invoked for the same
        partition more than once, the latest offset will be used on the next
        :meth:`~kafka.KafkaConsumer.poll`.

        Note: You may lose data if this API is arbitrarily used in the middle of
        consumption to reset the fetch offsets.

        Arguments:
            partition (TopicPartition): Partition for seek operation
            offset (int): Message offset in partition"""
    
    
    ### COLLECT INPUTS FOR THIS OPERATION ---------------------------------
    def get_offsets(self, partitions_set): # Targets Consumer
        
        self.get_total_offset(partitions_set) # Prints Partitions 
        partition_number = int(input('Select Partition #: '))
        offset_min = int(input('Enter Minimum Offset #: ')) ## CHECK IF 'OUT OF RANGE'
        offset_max = int(input('Enter Maximum Offset #: ')) ## CHECK IF 'OUT OF RANGE'

        print('SELECTED:',
              f'Partition: {partition_number}',
              f'Range: {offset_min} - {offset_max}',
              sep='\n')

        for offset in range(offset_min, offset_max):
            self.get_specified_offset(partition_number, offset)
        


oc = OffsetChoice()
oc.get_offsets()