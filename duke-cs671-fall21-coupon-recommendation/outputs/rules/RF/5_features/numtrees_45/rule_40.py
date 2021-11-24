def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[2]<=16:
				# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[2]>16:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=1:
				return 'True'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
