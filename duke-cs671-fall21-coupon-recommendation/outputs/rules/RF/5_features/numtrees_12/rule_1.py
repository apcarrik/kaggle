def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 55, "metric_value": 0.994, "depth": 2}
		if obj[2]<=9:
			# {"feature": "Distance", "instances": 42, "metric_value": 0.9984, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.9928, "depth": 4}
				if obj[3]>-1.0:
					# {"feature": "Coupon", "instances": 39, "metric_value": 0.9881, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>9:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[0]>1:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]>2.0:
					return 'False'
				else: return 'False'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.8813, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.7554, "depth": 3}
			if obj[2]>2:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[3]<=2.0:
						return 'True'
					elif obj[3]>2.0:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		elif obj[0]>3:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=5:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[2]>5:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
