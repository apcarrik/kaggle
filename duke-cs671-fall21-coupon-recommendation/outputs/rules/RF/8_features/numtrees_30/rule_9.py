def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[4]<=2.0:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[3]>1:
			# {"feature": "Passanger", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 4}
				if obj[7]<=2:
					# {"feature": "Education", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 1.0, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 7}
							if obj[1]>1:
								# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[1]<=1:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[7]>2:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	elif obj[4]>2.0:
		return 'True'
	else: return 'True'
