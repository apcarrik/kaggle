def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[8]>1:
		# {"feature": "Income", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[9]<=6:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[7]<=1:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[2]>3:
					# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[10]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=3:
					return 'True'
				else: return 'True'
			elif obj[7]>1:
				return 'False'
			else: return 'False'
		elif obj[9]>6:
			return 'True'
		else: return 'True'
	elif obj[8]<=1:
		return 'True'
	else: return 'True'
