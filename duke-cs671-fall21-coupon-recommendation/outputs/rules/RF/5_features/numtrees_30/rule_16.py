def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>4:
		# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 2}
		if obj[4]>1:
			# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[3]>-1.0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[0]<=3:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>3:
					return 'False'
				else: return 'False'
			elif obj[3]<=-1.0:
				return 'True'
			else: return 'True'
		elif obj[4]<=1:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[0]>2:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=2:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=4:
		# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=2:
				return 'True'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
