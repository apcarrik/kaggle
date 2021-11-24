def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[8]<=2.0:
		# {"feature": "Age", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[4]<=6:
			# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Passanger", "instances": 17, "metric_value": 0.9367, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[6]>0:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[12]<=1:
							# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[7]<=6:
								return 'True'
							elif obj[7]>6:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]>3:
									return 'False'
								elif obj[2]<=3:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]>1:
							# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[6]<=2:
					return 'True'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>6:
			# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]>2.0:
		return 'True'
	else: return 'True'
