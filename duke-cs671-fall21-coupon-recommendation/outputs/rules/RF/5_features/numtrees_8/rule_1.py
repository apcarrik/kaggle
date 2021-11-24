def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Coupon", "instances": 114, "metric_value": 0.9857, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Education", "instances": 71, "metric_value": 0.9229, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Occupation", "instances": 48, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=19.788371705248323:
					# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.8366, "depth": 5}
					if obj[3]<=3.0:
						return 'True'
					elif obj[3]>3.0:
						return 'True'
					else: return 'True'
				elif obj[2]>19.788371705248323:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 4}
				if obj[2]<=8:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[3]<=2.0:
						return 'True'
					elif obj[3]>2.0:
						return 'True'
					else: return 'True'
				elif obj[2]>8:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[3]<=2.0:
						return 'False'
					elif obj[3]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[0]>3:
			# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.9808, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Occupation", "instances": 39, "metric_value": 0.9418, "depth": 4}
				if obj[2]<=11:
					# {"feature": "Education", "instances": 29, "metric_value": 0.8498, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[2]>11:
					# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>2:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[0]>1:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=11:
				# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]>1.0:
						return 'False'
					elif obj[3]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]>11:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
