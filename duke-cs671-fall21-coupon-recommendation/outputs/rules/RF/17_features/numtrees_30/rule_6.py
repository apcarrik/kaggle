def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[9]>1:
		# {"feature": "Bar", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[12]<=2.0:
			# {"feature": "Direction_same", "instances": 18, "metric_value": 0.65, "depth": 3}
			if obj[15]<=0:
				# {"feature": "Age", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[6]>0:
					return 'True'
				elif obj[6]<=0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[15]>0:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>2:
						return 'True'
					elif obj[6]<=2:
						return 'False'
					else: return 'False'
				elif obj[2]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[12]>2.0:
			return 'False'
		else: return 'False'
	elif obj[9]<=1:
		# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[7]<=1:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[10]>6:
				return 'False'
			elif obj[10]<=6:
				# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]>2:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
