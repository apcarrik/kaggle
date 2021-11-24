def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[9]<=7:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[11]<=2.0:
				# {"feature": "Age", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[6]<=6:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[13]<=2.0:
						# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[4]>0:
							# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[3]>0:
								# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[10]<=4:
									return 'True'
								elif obj[10]>4:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[13]>2.0:
						return 'False'
					else: return 'False'
				elif obj[6]>6:
					return 'False'
				else: return 'False'
			elif obj[11]>2.0:
				return 'False'
			else: return 'False'
		elif obj[9]>7:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
