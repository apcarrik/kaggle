def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 47, "metric_value": 0.9734, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Occupation", "instances": 34, "metric_value": 0.9082, "depth": 3}
			if obj[3]<=12:
				# {"feature": "Bar", "instances": 30, "metric_value": 0.9481, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.8767, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Direction_same", "instances": 18, "metric_value": 0.9911, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 8}
								if obj[1]>1:
									return 'True'
								elif obj[1]<=1:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						elif obj[7]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'True'
					else: return 'True'
				elif obj[4]>2.0:
					return 'False'
				else: return 'False'
			elif obj[3]>12:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[1]>1:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]<=11:
					# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4]>1.0:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]>3.0:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]>1:
								return 'True'
							elif obj[7]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]<=3.0:
							return 'True'
						else: return 'True'
					elif obj[4]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[3]>11:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'
