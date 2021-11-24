def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[6]>0:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[10]>1:
			# {"feature": "Bar", "instances": 25, "metric_value": 0.9988, "depth": 3}
			if obj[12]<=2.0:
				# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 20, "metric_value": 0.9928, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[13]<=3.0:
							# {"feature": "Distance", "instances": 15, "metric_value": 0.9183, "depth": 7}
							if obj[16]<=2:
								# {"feature": "Direction_same", "instances": 14, "metric_value": 0.8631, "depth": 8}
								if obj[15]<=0:
									# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.684, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[9]>1:
												return 'True'
											elif obj[9]<=1:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]>0:
										return 'False'
									else: return 'False'
								elif obj[15]>0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[16]>2:
								return 'True'
							else: return 'True'
						elif obj[13]>3.0:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[12]>2.0:
				return 'False'
			else: return 'False'
		elif obj[10]<=1:
			return 'True'
		else: return 'True'
	elif obj[6]<=0:
		return 'False'
	else: return 'False'
