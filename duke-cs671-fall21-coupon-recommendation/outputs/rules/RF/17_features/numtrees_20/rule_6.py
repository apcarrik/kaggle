def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[11]<=7:
		# {"feature": "Coffeehouse", "instances": 45, "metric_value": 0.971, "depth": 2}
		if obj[13]>1.0:
			# {"feature": "Occupation", "instances": 26, "metric_value": 0.9829, "depth": 3}
			if obj[10]<=10:
				# {"feature": "Bar", "instances": 21, "metric_value": 0.9984, "depth": 4}
				if obj[12]<=1.0:
					# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[9]>0:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[3]>1:
								return 'False'
							elif obj[3]<=1:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]>2:
								return 'True'
							elif obj[2]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]<=0:
						return 'True'
					else: return 'True'
				elif obj[12]>1.0:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[14]>0.0:
						return 'False'
					elif obj[14]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]>10:
				return 'True'
			else: return 'True'
		elif obj[13]<=1.0:
			# {"feature": "Age", "instances": 19, "metric_value": 0.6292, "depth": 3}
			if obj[6]>0:
				# {"feature": "Children", "instances": 18, "metric_value": 0.5033, "depth": 4}
				if obj[8]<=0:
					return 'False'
				elif obj[8]>0:
					# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[11]>7:
		return 'True'
	else: return 'True'
