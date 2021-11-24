def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[9]<=5:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[8]>6:
			# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[7]<=2:
				# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]>1:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[7]>2:
				return 'False'
			else: return 'False'
		elif obj[8]<=6:
			# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[12]>0.0:
				return 'True'
			elif obj[12]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[9]>5:
		return 'True'
	else: return 'True'
