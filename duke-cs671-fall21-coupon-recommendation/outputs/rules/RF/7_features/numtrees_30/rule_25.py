def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 27, "metric_value": 0.8767, "depth": 2}
		if obj[3]<=12:
			# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.7554, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Passanger", "instances": 19, "metric_value": 0.8315, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[6]>2:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[3]>12:
			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=2:
				return 'True'
			elif obj[2]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
