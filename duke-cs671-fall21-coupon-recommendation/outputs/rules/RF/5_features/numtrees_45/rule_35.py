def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[3]>0.0:
			# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=7:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				elif obj[2]>7:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[3]<=0.0:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>3:
		# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[3]<=2.0:
			# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[4]>1:
				return 'False'
			elif obj[4]<=1:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
