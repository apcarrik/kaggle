def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 26, "metric_value": 0.9612, "depth": 2}
		if obj[4]>1:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[2]>1:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[3]<=0.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		elif obj[4]<=1:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[2]<=10:
				# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0.0:
						return 'True'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[2]>10:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[2]>7:
			return 'False'
		elif obj[2]<=7:
			# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]>1.0:
				return 'False'
			elif obj[3]<=1.0:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
