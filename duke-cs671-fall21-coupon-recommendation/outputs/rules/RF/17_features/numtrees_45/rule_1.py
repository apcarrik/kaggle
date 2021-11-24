def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]<=6:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[10]>3:
			# {"feature": "Income", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[11]>0:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=2:
							return 'False'
						elif obj[3]>2:
							# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]<=0:
								return 'False'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[14]>1.0:
					return 'True'
				else: return 'True'
			elif obj[11]<=0:
				return 'False'
			else: return 'False'
		elif obj[10]<=3:
			return 'False'
		else: return 'False'
	elif obj[6]>6:
		return 'False'
	else: return 'False'
