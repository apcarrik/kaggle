def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.5033, "depth": 2}
		if obj[3]<=5:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'True'
						else: return 'True'
					elif obj[4]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>5:
			return 'True'
		else: return 'True'
	elif obj[2]>1:
		# {"feature": "Passanger", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[3]<=11:
				# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			elif obj[3]>11:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'True'
