def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[12]<=2.0:
		# {"feature": "Education", "instances": 43, "metric_value": 0.9682, "depth": 2}
		if obj[9]>1:
			# {"feature": "Passanger", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[0]>0:
				# {"feature": "Age", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[6]<=6:
					# {"feature": "Distance", "instances": 19, "metric_value": 0.8997, "depth": 5}
					if obj[16]>1:
						# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[3]>3:
							# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[11]>0:
								return 'False'
							elif obj[11]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]<=3:
							# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]>1:
									return 'False'
								elif obj[2]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[16]<=1:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[6]>6:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[9]<=1:
			# {"feature": "Distance", "instances": 21, "metric_value": 0.7025, "depth": 3}
			if obj[16]>1:
				# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[2]>0:
					# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[13]<=3.0:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[15]<=0:
							return 'True'
						elif obj[15]>0:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[13]>3.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[16]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[12]>2.0:
		return 'True'
	else: return 'True'
