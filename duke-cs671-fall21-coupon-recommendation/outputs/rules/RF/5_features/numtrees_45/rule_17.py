def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[1]>1:
			# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[4]<=2:
					return 'False'
				elif obj[4]>2:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=4:
						return 'False'
					elif obj[2]>4:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=10:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=0.0:
						return 'True'
					elif obj[3]>0.0:
						return 'True'
					else: return 'True'
				elif obj[4]>1:
					return 'True'
				else: return 'True'
			elif obj[2]>10:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'
