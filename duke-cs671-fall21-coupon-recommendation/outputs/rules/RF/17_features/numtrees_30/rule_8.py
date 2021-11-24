def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[9]>0:
		# {"feature": "Maritalstatus", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[7]>0:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[10]>5:
				# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[11]>2:
					return 'False'
				elif obj[11]<=2:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=2:
						return 'True'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]<=5:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]<=3:
						return 'True'
					elif obj[11]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[7]<=0:
			# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[12]>-1.0:
				return 'False'
			elif obj[12]<=-1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[9]<=0:
		# {"feature": "Time", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[2]<=3:
			return 'True'
		elif obj[2]>3:
			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
