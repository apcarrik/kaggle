def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[6]>1:
				# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=11:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>1.0:
								return 'True'
							elif obj[4]<=1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>11:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			elif obj[6]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
