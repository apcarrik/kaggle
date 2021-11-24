def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[11]<=5:
		# {"feature": "Coupon_validity", "instances": 24, "metric_value": 0.8113, "depth": 2}
		if obj[4]>0:
			# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[12]<=2.0:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[10]<=12:
						return 'True'
					elif obj[10]>12:
						return 'False'
					else: return 'False'
				elif obj[12]>2.0:
					return 'False'
				else: return 'False'
			elif obj[9]>2:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	elif obj[11]>5:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[10]<=13:
				return 'False'
			elif obj[10]>13:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=1:
					return 'True'
				elif obj[2]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
