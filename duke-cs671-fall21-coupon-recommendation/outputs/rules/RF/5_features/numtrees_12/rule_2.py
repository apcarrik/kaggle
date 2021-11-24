def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 62, "metric_value": 0.9072, "depth": 2}
		if obj[2]>0:
			# {"feature": "Restaurant20to50", "instances": 60, "metric_value": 0.8813, "depth": 3}
			if obj[3]<=3.0:
				# {"feature": "Education", "instances": 58, "metric_value": 0.8498, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 55, "metric_value": 0.8699, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[3]>3.0:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Distance", "instances": 21, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9641, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]>2.0:
					return 'True'
				else: return 'True'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>10:
			return 'True'
		else: return 'True'
	else: return 'False'
