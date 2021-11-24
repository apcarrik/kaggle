def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[6]<=4:
		# {"feature": "Passanger", "instances": 38, "metric_value": 0.998, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Education", "instances": 23, "metric_value": 0.8865, "depth": 3}
			if obj[9]<=4:
				# {"feature": "Income", "instances": 21, "metric_value": 0.7919, "depth": 4}
				if obj[11]<=7:
					# {"feature": "Occupation", "instances": 19, "metric_value": 0.6292, "depth": 5}
					if obj[10]<=11:
						return 'False'
					elif obj[10]>11:
						# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]>7:
					return 'True'
				else: return 'True'
			elif obj[9]>4:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[2]>2:
				# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[3]>2:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[10]>1:
						return 'True'
					elif obj[10]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]<=2:
					return 'False'
				else: return 'False'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[6]>4:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.3912, "depth": 2}
		if obj[12]>-1.0:
			return 'True'
		elif obj[12]<=-1.0:
			return 'False'
		else: return 'False'
	else: return 'True'
