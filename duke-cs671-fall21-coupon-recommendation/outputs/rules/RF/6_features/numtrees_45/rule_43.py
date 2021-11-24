def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]>1:
		# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[3]>1:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[5]<=2:
					return 'True'
				elif obj[5]>2:
					return 'False'
				else: return 'False'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]>10:
				return 'False'
			elif obj[3]<=10:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
