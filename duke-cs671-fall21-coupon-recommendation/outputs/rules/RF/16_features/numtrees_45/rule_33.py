def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[8]<=3:
		# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[9]<=20:
				# {"feature": "Children", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[6]<=1:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[6]>1:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>0:
					# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[10]<=7:
						return 'False'
					elif obj[10]>7:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]>20:
				return 'True'
			else: return 'True'
		elif obj[13]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[8]>3:
		return 'True'
	else: return 'True'
