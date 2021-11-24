def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.9544, "depth": 3}
			if obj[3]>3:
				# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Bar", "instances": 19, "metric_value": 0.998, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Passanger", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Distance", "instances": 14, "metric_value": 0.9403, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Direction_same", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[6]>0:
									return 'True'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>2:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=2:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>2.0:
						return 'False'
					else: return 'False'
				elif obj[5]>2.0:
					return 'True'
				else: return 'True'
			elif obj[3]<=3:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		return 'True'
	else: return 'True'
