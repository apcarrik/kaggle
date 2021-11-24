def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Passanger", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 16, "metric_value": 1.0, "depth": 3}
			if obj[3]<=6:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]>2.0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>6:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=0.0:
					return 'True'
				elif obj[4]>0.0:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		return 'True'
	else: return 'True'
