def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[11]<=7:
		# {"feature": "Passanger", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[7]>0:
				# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[10]<=4:
							return 'False'
						elif obj[10]>4:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			elif obj[7]<=0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[13]>0.0:
				return 'True'
			elif obj[13]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[11]>7:
		return 'False'
	else: return 'False'
