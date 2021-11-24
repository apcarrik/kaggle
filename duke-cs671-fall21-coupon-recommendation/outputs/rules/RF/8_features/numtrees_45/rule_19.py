def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]<=11:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[7]>1:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[7]<=1:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0:
						return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]>1.0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>11:
		return 'False'
	else: return 'False'
