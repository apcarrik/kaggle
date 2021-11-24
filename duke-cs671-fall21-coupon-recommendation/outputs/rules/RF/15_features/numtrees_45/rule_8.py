def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[5]>1:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[8]<=9:
			# {"feature": "Income", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[9]<=3:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[14]<=1:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[11]>0.0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]>2:
							return 'True'
						elif obj[2]<=2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[11]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[14]>1:
					return 'False'
				else: return 'False'
			elif obj[9]>3:
				return 'True'
			else: return 'True'
		elif obj[8]>9:
			return 'False'
		else: return 'False'
	elif obj[5]<=1:
		# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[9]<=6:
			return 'True'
		elif obj[9]>6:
			return 'False'
		else: return 'False'
	else: return 'True'
