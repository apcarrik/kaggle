def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[1]>1:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[2]>1:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[3]>5:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[4]<=1.0:
						return 'False'
					elif obj[4]>1.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=3:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]<=5:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>1.0:
							return 'True'
						elif obj[4]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			return 'False'
		else: return 'False'
	elif obj[5]<=1:
		# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=8:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]<=1:
							return 'True'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[3]>8:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
