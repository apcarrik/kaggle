def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[4]<=3.0:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[6]>1:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[3]<=7:
				return 'True'
			elif obj[3]>7:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]>1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]<=1:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>4:
						return 'True'
					elif obj[3]<=4:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[2]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[4]>3.0:
		return 'False'
	else: return 'False'
