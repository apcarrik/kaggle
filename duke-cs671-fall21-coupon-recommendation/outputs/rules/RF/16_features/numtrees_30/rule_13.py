def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[13]<=2.0:
		# {"feature": "Occupation", "instances": 30, "metric_value": 1.0, "depth": 2}
		if obj[9]>4:
			# {"feature": "Coupon_validity", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[4]>0:
				# {"feature": "Children", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[7]<=0:
					return 'False'
				elif obj[7]>0:
					return 'True'
				else: return 'True'
			elif obj[4]<=0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[10]>2:
						return 'False'
					elif obj[10]<=2:
						return 'True'
					else: return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=4:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[3]>0:
				# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[8]>0:
					return 'True'
				elif obj[8]<=0:
					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[13]>2.0:
		return 'True'
	else: return 'True'
