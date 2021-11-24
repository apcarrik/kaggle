def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[10]<=10:
		# {"feature": "Coupon", "instances": 28, "metric_value": 0.9403, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Income", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[11]<=3:
				# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[6]<=1:
					# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[2]>1:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[9]>0:
							return 'True'
						elif obj[9]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]>1:
					return 'True'
				else: return 'True'
			elif obj[11]>3:
				return 'False'
			else: return 'False'
		elif obj[3]>1:
			# {"feature": "Education", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[9]<=1:
				return 'True'
			elif obj[9]>1:
				# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[6]<=2:
					return 'True'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[10]>10:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[3]>0:
			return 'False'
		elif obj[3]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
