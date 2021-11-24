def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Distance", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[6]>1:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[6]<=1:
			# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[2]<=2:
				return 'True'
			elif obj[2]>2:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
