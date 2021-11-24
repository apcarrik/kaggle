def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[3]<=12:
		# {"feature": "Distance", "instances": 30, "metric_value": 0.9871, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Education", "instances": 26, "metric_value": 0.9306, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Coupon", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[1]>3:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=3:
					return 'True'
				else: return 'True'
			elif obj[2]>1:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[1]>0:
					# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[4]>-1.0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[4]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	elif obj[3]>12:
		return 'False'
	else: return 'False'
