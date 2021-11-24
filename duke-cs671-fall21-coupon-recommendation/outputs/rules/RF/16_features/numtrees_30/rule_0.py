def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>0:
		# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.9629, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Coupon", "instances": 27, "metric_value": 0.9911, "depth": 3}
			if obj[3]>0:
				# {"feature": "Time", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Bar", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[11]<=1.0:
						return 'True'
					elif obj[11]>1.0:
						# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=0:
							return 'True'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]>2:
					# {"feature": "Income", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[10]>1:
						return 'False'
					elif obj[10]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=0:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[13]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
