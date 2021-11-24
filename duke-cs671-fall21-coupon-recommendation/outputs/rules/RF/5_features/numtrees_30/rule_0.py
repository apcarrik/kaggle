def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[2]<=10:
		# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.6913, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Education", "instances": 15, "metric_value": 0.3534, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]>2:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>1.0:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]>10:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=2:
					return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			elif obj[3]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
