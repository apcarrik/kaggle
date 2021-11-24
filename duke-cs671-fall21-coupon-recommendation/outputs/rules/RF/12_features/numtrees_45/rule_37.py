def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[7]>0.0:
		# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[9]>0.0:
			return 'True'
		elif obj[9]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[7]<=0.0:
		# {"feature": "Direction_same", "instances": 11, "metric_value": 0.994, "depth": 2}
		if obj[10]<=0:
			# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[11]>1:
				# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[4]<=6:
					return 'True'
				elif obj[4]>6:
					return 'False'
				else: return 'False'
			elif obj[11]<=1:
				return 'False'
			else: return 'False'
		elif obj[10]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
