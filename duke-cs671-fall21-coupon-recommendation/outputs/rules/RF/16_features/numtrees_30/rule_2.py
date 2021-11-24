def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[9]<=10:
				# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[10]<=3:
					return 'True'
				elif obj[10]>3:
					return 'False'
				else: return 'False'
			elif obj[9]>10:
				# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]>1:
					return 'False'
				elif obj[6]<=1:
					# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[10]>2:
						return 'True'
					elif obj[10]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[3]>2:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[8]>0:
			return 'False'
		elif obj[8]<=0:
			# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[5]>0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=0:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>0:
					return 'False'
				else: return 'False'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
