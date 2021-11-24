def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=16:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Education", "instances": 19, "metric_value": 0.8997, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[0]<=3:
					return 'True'
				elif obj[0]>3:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[0]<=3:
					return 'True'
				elif obj[0]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	elif obj[2]>16:
		return 'False'
	else: return 'False'
