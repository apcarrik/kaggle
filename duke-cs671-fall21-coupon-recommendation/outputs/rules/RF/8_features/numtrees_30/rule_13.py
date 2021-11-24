def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]>1:
		# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.9968, "depth": 2}
		if obj[5]<=2.0:
			# {"feature": "Coupon", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[1]>1:
				# {"feature": "Passanger", "instances": 22, "metric_value": 1.0, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Bar", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 12, "metric_value": 1.0, "depth": 6}
						if obj[2]<=1:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[7]<=1:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[7]>1:
								return 'False'
							else: return 'False'
						elif obj[2]>1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[6]<=0:
								return 'True'
							elif obj[6]>0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>0.0:
							return 'False'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		elif obj[5]>2.0:
			return 'True'
		else: return 'True'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
