def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[7]<=3:
		# {"feature": "Coupon", "instances": 28, "metric_value": 0.9403, "depth": 2}
		if obj[2]>1:
			# {"feature": "Age", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[8]<=14:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[0]<=2:
						return 'True'
					elif obj[0]>2:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=2:
							return 'False'
						elif obj[1]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]>14:
					return 'False'
				else: return 'False'
			elif obj[5]>2:
				# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[9]>0:
						return 'False'
					elif obj[9]<=0:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[10]>0.0:
							return 'False'
						elif obj[10]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[7]>3:
		return 'True'
	else: return 'True'
