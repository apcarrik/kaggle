def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=10:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[2]>10:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
