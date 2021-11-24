def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[10]<=3.0:
		# {"feature": "Income", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[9]<=4:
			# {"feature": "Age", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[5]>2:
				# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[7]>1:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]>2:
						return 'False'
					elif obj[8]<=2:
						return 'True'
					else: return 'True'
				elif obj[7]<=1:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[8]<=5:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[8]>5:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[5]<=2:
				return 'False'
			else: return 'False'
		elif obj[9]>4:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[1]>0:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=0:
						return 'False'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[10]>3.0:
		return 'True'
	else: return 'True'
