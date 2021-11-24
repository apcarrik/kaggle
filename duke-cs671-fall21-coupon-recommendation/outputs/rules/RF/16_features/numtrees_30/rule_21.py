def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[9]<=14:
		# {"feature": "Bar", "instances": 27, "metric_value": 0.9911, "depth": 2}
		if obj[11]<=2.0:
			# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Income", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[10]<=3:
					# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[6]>0:
						return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				elif obj[10]>3:
					# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4]>0:
						# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[11]>2.0:
			return 'True'
		else: return 'True'
	elif obj[9]>14:
		return 'False'
	else: return 'False'
