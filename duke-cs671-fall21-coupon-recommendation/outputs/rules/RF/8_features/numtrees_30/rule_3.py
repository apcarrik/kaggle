def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 32, "metric_value": 0.9745, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Bar", "instances": 27, "metric_value": 0.9751, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 5}
					if obj[7]>1:
						# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[3]>4:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[1]>3:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=4:
							return 'False'
						else: return 'False'
					elif obj[7]<=1:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[3]<=11:
							# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[1]>2:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[1]<=2:
								return 'True'
							else: return 'True'
						elif obj[3]>11:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=0:
								return 'False'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			elif obj[5]>2.0:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
