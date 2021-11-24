def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[10]>0.0:
		# {"feature": "Income", "instances": 23, "metric_value": 0.9321, "depth": 2}
		if obj[9]>0:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Education", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[7]<=3:
					return 'True'
				elif obj[7]>3:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>2:
						return 'True'
					elif obj[1]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[5]<=2:
					return 'False'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[10]<=0.0:
		# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[11]<=2.0:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
