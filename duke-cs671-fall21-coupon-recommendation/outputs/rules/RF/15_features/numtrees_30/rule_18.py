def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[9]>1:
		# {"feature": "Education", "instances": 29, "metric_value": 0.9576, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 3}
			if obj[2]>2:
				# {"feature": "Age", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[5]>2:
					return 'True'
				elif obj[5]<=2:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[8]<=10:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[8]>10:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=2:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]>2:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[11]>1.0:
				return 'True'
			elif obj[11]<=1.0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[9]<=1:
		return 'False'
	else: return 'False'
