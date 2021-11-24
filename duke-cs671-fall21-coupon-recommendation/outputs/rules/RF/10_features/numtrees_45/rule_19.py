def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[7]>0.0:
		# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[6]<=3.0:
			# {"feature": "Bar", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[9]<=1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=3:
								return 'True'
							elif obj[1]>3:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]>2:
									return 'True'
								elif obj[2]<=2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					elif obj[9]>1:
						return 'True'
					else: return 'True'
				elif obj[8]>0:
					return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				return 'True'
			else: return 'True'
		elif obj[6]>3.0:
			return 'False'
		else: return 'False'
	elif obj[7]<=0.0:
		return 'False'
	else: return 'False'
